// from data.js
var tableData = data;
var tbody = d3.select("tbody");

// YOUR CODE HERE!
console.log(tableData)

data.forEach(function(alien){
    console.log(alien);
    var row = tbody.append("tr");
    Object.entries(alien).forEach(function([key, value]) {
        console.log(key, value);
        var cell = tbody.append("td");
        cell.text(value);
    });
});

var submit = d3.select("#submit");

submit.on("click",function() {
  d3.event.preventDefault();
  var inputElement = d3.select("#date");
  var inputValue = inputElement.property("value");
  console.log(inputValue);
  console.log(alien);
  var filteredData = alien.filter(alien => alien.datetime === inputValue);

  console.log(filteredData);

})