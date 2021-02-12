//using fetch to send a get request to get the meme content
fetch('https://xmeme.shahmeet.me/api/memes/') //using promises
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
        console.log(resu.length-1);
        //fetching the latest 100
        if(resu.length-1<=100) //The number of memes posted is less than 100 that's max number of memes is only less than 100 in that scenario we post out all the memes we have
        {
          //starting from the last so that latest memes can be viewed first
          for (i=resu.length-1;i>=0;i--) //posting all the memes as number of posted memes is less than 100
          {
            mname = resu[i].name; 
            mcaption = resu[i].caption;
            mimageurl = resu[i].url;

            //storing the memes content in res
            res+= "<div id='memebox'><h4>Name : "+mname+"</h4><h4>caption : "+mcaption+"</h4><img src ="+mimageurl+" alt='The url is valid but does not contain an image' height='100%' width='100%'></img><br></div>";
        
        
          }
        }
        else //when number of memes posted is more than 100 then we display only the latest 100
        {
          //starting from the last so that latest memes can be viewed first
          for (i=resu.length-1;i>=(resu.length-1)-100;i--) //posting the latest 100 memes posted as number of posted memes is greater than 100
          {
            mname = resu[i].name; 
            mcaption = resu[i].caption;
            mimageurl = resu[i].url;

        //storing the memes content in res
          res+= "<div id='memebox'><h4>Name : "+mname+"</h4><img src ="+mimageurl+" alt='The url is valid but does not contain an image' height='100%' width='100%'></img><h4>caption : "+mcaption+"</h4><br></div>";
        
        
          }
        }
        document.getElementById("test").innerHTML = res; //rendering res and displaying the content on web page.
  
      
    })
    .catch(function(err) {
        console.log('Fetch problem: '); //catch function to check for error, if any then shall be printed on console.
    });
