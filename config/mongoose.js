const mongoose = require("mongoose");

const db =
  "mongodb+srv://localhost80:pass1234@cluster0.5w2ht.mongodb.net/trending?retryWrites=true&w=majority";

mongoose
  .connect(db, {
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true,
    useFindAndModify: false
  })
  .then(() => {
    console.log("connection success");
  })
  .catch(err => {
    console.log("Unsuccessful");
  });
