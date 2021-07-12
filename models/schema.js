const mongoose = require("mongoose");
const uniqueValidator = require("mongoose-unique-validator");
const Schema = mongoose.Schema;

const videoSchema = new Schema({
  title: {
    type: String,
    required: true
  },
  url: {
    type: String,
    required: true,
    unique: true
  },
  channel_name: {
    type: String,
    required: true
  },
  subscribers: {
    type: String,
    required: true
  },
  views: {
    type: String,
    required: true
  },
  likes: {
    type: String,
    required: true
  },
  dislikes: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  channel_thumbnail: {
    type: String,
    required: true
  }
});
videoSchema.plugin(uniqueValidator);

module.exports = mongoose.model("videos", videoSchema);
