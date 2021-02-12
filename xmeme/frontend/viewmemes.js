//using fetch to send a get request to get the meme content
fetch('http://127.0.0.1:8000/api/memes/') //using promises
    .then(function(response) { 
        //console.log(response.json())
        return response.json();

    })
    .then(function(json) {
        let resu = json; //this has all the content in json format
        console.log(resu); //printing it in console just to check if we are going in the right path, can be ignored.
        var res = ""; //declaring the result variable where we shall store content and render it on the web page

        //mname - stores meme name
        //mcaption - stores meme caption
        //mimageurl - stores meme image url
        var mname,mcaption,mimageurl; 

        //starting from the last so that latest memes can be viewed first
        for (i=resu.length-1;i>=0;i--) {
        mname = resu[i].name; 
        mcaption = resu[i].caption;
        mimageurl = resu[i].url;

        //storing the memes content in res
        res+= "<div id='memebox'><h4>Name : "+mname+"</h4><img src ="+mimageurl+" alt='Image ain't possible height='100%' width='100%'></img><h4>caption : "+mcaption+"</h4><br></div>";
        
        
        }
        document.getElementById("test").innerHTML = res; //rendering res and displaying the content on web page.
  
      
    })
    .catch(function(err) {
        console.log('Fetch problem: '); //catch function to check for error, if any then shall be printed on console.
    });
