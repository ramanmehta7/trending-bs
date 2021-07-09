const { spawn } = require("child_process");

const fileName = "hello-world.py";
exports.listVideos = (req, res, next) => {
  const data = spawn("python", [fileName]);
  data.stdout.on("data", data => {
    console.log(`stdout ${data}`);
  });

  data.stderr.on("data", data => {
    console.log(`stderr ${data}`);
  });

  data.on("error", error => {
    console.log(`Error ${error.message}`);
  });
  res.send("ListVideos");
};
