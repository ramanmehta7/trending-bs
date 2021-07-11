const mongoose = require('mongoose');

const videoSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    url: {
        type: String
    }
});

const Videos = mongoose.model('Videos', videoSchema);

module.exports = Videos;