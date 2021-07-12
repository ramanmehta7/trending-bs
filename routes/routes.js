const express = require("express");
const router = express.Router();

const contollers = require("../controllers/controller");

router.get("/listvideos", contollers.listVideos);
router.get("/runScript", contollers.runScript);
router.get("/details/:url", contollers.getVideoDetails);

module.exports = router;
