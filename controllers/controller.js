const { spawn } = require("child_process");
const VideoModel = require("../models/schema");

const fileName = "data.py";

exports.runScript = (req, res, next) => {
  const data = spawn("python3", [fileName]);
  data.stdout.on("data", data => {
    console.log(`stdout ${data}`);
    res.status(200).json({
      success: true,
      message: "Database Populated"
    });
  });

  data.stderr.on("data", data => {
    console.log(`stderr ${data}`);
    res.status(200).json({
      success: false,
      message: "STDError"
    });
  });

  data.on("error", error => {
    console.log(`Error ${error.message}`);
    res.status(200).json({
      success: false,
      message: "Error Occured"
    });
  });
};
exports.listVideos = (req, res, next) => {
  VideoModel.find()
    .then(videos => {
      console.log(videos);
      res.status(200).json({
        videos: videos,
        success: true
      });
    })
    .catch(e => {
      console.log("List Video Error ", e);
      res.status(200).json({
        success: false
      });
    });
};

exports.getVideoDetails = (req, res, next) => {
  const url = req.params.url;
  console.log(url);
  VideoModel.find({
    url: url
  })
    .then(details => {
      console.log(details);
      res.status(200).json({
        details: details,
        success: true
      });
    })
    .catch(e => {
      console.log("List Video Error ", e);
      res.status(200).json({
        success: false
      });
    });
};
