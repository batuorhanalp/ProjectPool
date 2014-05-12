'use strict';

/**
 * Module dependencies.
 */
var mongoose = require('mongoose'),
    Schema = mongoose.Schema;


/**
 * Article Schema
 */
var IdeaSchema = new Schema({
    created: {
        type: Date,
        default: Date.now
    },
    name: {
        type: String,
        default: '',
        trim: true
    },
    summary: {
        type: String,
        default: '',
        trim: true
    },
    detail: {
        type: String,
        default: '',
        trim: true
    },
    offerredBrands: [{ type: Schema.ObjectId, ref: 'Brand' }],
    dealtBrands: [{ type: Schema.ObjectId, ref: 'Brand' }],
    categories: [{ type: Schema.ObjectId, ref: 'Category' }],
    budget: {
        type: Schema.ObjectId,
        ref: 'Budget',
    },
    date: {
        type: Date
    },
    createdBy: {
        type: Schema.ObjectId,
        ref: 'User'
    }
});

/**
 * Validations
 */
IdeaSchema.path('name').validate(function(name) {
    return name.length;
}, 'Name cannot be blank');


/**
 * Statics
 */
IdeaSchema.statics.load = function(id, cb) {
    this.findOne({
        _id: id
    }).populate('user', 'name username').exec(cb);
};

mongoose.model('Idea', IdeaSchema);
