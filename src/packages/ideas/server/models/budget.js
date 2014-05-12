'use strict';

/**
 * Module dependencies.
 */
var mongoose = require('mongoose'),
    Schema = mongoose.Schema;


/**
 * Article Schema
 */
var BudgetSchema = new Schema({
    created: {
        type: Date,
        default: Date.now
    },
    start: {
        type: Number,
        default: 0
    },
    end: {
        type: Number,
        default: 0
    }
});


mongoose.model('Budget', BudgetSchema);
