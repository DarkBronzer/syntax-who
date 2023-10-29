import * as express from 'express';
import * as mongoose from "mongoose";
import Shops from './models/shops';

const app = express();
app.listen(5000, () => {
    console.log('started my server');
});

mongoose.connect('mongodb+srv://shagun:shagun@cluster0.ct9co.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true})
    .then((data) => {
        console.log('connected to database');
    });

app.get('/shops', (req, res, next) => {
    const options = {
        location: {
            $geoWithin: {
                $centerSphere: [[29.8696739,77.8924046], 25 / 3963.2]
            }
        }
    }
    Shops.find(options).then(data => {
        res.send(data);
    })
})
