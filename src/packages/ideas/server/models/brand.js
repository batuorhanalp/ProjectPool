'use strict';

/**
 * module dependencies.
 */
var mongoose = require('mongoose'),
    Schema = mongoose.Schema;


/**
 * brand schema
 */
var BrandSchema = new Schema({        
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
BrandSchema.path('name').validate(function(name) {
    return name.length;
}, 'marka ismi boş bırakılamaz.');


mongoose.model('Brand', BrandSchema);
