'use strict';

var ideas = require('../controllers/ideas');

// The Package is past automatically as first parameter
module.exports = function(Ideas, app, auth, database) {

    app.route('/ideas')
        .get(ideas.all)
        .post(ideas.create);

    app.get('/ideas/example/anyone', function(req, res, next) {
        res.send('Anyone can access this');
    });

    app.get('/ideas/example/auth', auth.requiresLogin, function(req, res, next) {
        res.send('Only authenticated users can access this');
    });

    app.get('/ideas/example/admin', auth.requiresAdmin, function(req, res, next) {
        res.send('Only users with Admin role can access this');
    });

    app.get('/ideas/example/render', function(req, res, next) {
        Ideas.render('index', {
            package: 'ideas'
        }, function(err, html) {
            //Rendering a view from the Package server/views
            res.send(html);
        });
    });
};
