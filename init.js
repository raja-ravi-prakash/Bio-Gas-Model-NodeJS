const express = require("express");
var ex = require("shelljs").exec;
const app = express();
var cors = require("cors");

app.use(cors());
app.use(express.json());
app.use(express.static("public"));

app.post("/data", cors(), function (req, res) {
  console.log(req.body);
  let year = req.body.year;
  let month = req.body.month;
  let day = req.body.day;
  let cmd = "python model/sample.py " + year + " " + month + " " + day;
  console.log(cmd);
  var child = ex(cmd, { async: true });
  child.stdout.on("data", function (data) {
    res.send(data);
  });
});

app.listen(80, console.log("Running...."));
