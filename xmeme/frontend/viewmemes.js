fetch('http://127.0.0.1:8000/api/memes/').then(function(response) {
  return response.json();
}).then(function(json) {
  let res = json;
  console.log(res);
}).catch(function(err) {
  console.log('Fetch problem: ');
});