const express = require("express");
const router = express.Router();

const contollers = require("../controllers/controller");

router.get("/listvideos", contollers.listVideos);

module.exports = router;
