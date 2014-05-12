'use strict';

/**
 * Module dependencies
 */
var mongoose = require('mongoose'),
    Idea = mongoose.model('Idea');


/**
 * Crate an idea
 */
exports.create = function(req, res) {
    var idea = new Idea(req.body);
    idea.createdBy = req.user;

    idea.save(function(err) {
        if (err) {
            res.render('error', {
                status: 500
            });
            return;
        }

        res.jsonp(idea);
    });
};

/**
 * List all ideas
 */
exports.all = function(req, res) {
    Idea.find().sort('-created').populate('user', 'name username').exec(function(err, ideas) {
        if (err) {
            res.render('error', {
                status: 500
            });
            return;
        }

        res.jsonp(ideas);
    });
};
