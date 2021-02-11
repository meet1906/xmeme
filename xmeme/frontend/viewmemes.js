function test1 {
fetch('http://127.0.0.1:8000/api/memes/')
.then(function(response) {
  return response.json();
})
.then(function(json) {
  let resu = json;
  console.log(resu);
  var res;
  var mname,mcaption,mimageurl;
  for (i=0;i<=resu.length;i++) {
	mname = resu[i].name;
	mcaption = resu[i].caption;
	mimageurl = resu[i].url;

	res+= "<h4>Name : </h4>"+mname+"<h4>caption : </h4>"+"<img src ="+mimageurl+" alt='Image ain't possible></img>";
   }

document.getElementById("test").innerHTML = res;
})
.catch(function(err) {
  console.log('Fetch problem: ');
});

}


