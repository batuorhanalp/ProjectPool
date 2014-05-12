'use strict';

/**
 * module dependencies.
 */
var mongoose = require('mongoose'),
    Schema = mongoose.Schema;


/**
 * category schema
 */
var CategorySchema = new Schema({        
    name: {
        type: String,
        default: '',
        trim: true
    },
    created: {
        type: Date,
        default: Date.now
    }
});


/**
 * validations
 */
CategorySchema.path('name').validate(function(name) {
    return name.length;
}, 'marka ismi boş bırakılamaz.');


mongoose.model('Category', CategorySchema);
