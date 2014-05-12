'use strict';


require('../../server/models/brand');
require('../../server/models/budget');
require('../../server/models/idea');

/**
 * Module dependencies.
 */
var should = require('should'),
    mongoose = require('mongoose'),
    User = mongoose.model('User'),
    Brand = mongoose.model('Brand'),
    Budget = mongoose.model('Budget'),
    Category = mongoose.model('Category'),
    Idea = mongoose.model('Idea')
    ;

// Globals
var brand;
var idea;
var user;
var budget;

// Tests
describe('<Unit Test>', function() {
    describe('Model Brand:', function() {
        beforeEach(function(done) {
            brand = new Brand({
                name: 'Sample Brand'
            });
            done();
        });

        describe('Method Save', function() {
            it('should save without problems', function(done) {
                return brand.save(function(err) {
                    should.not.exist(err);
                    done();
                });
            });

            it('should not save without a name', function(done) {
                brand.name = '';

                return brand.save(function(err) {
                    should.exist(err);
                    done();
                });
            });

        });

        afterEach(function(done) {
            brand.remove();
            done();
        });

    });

    describe('Model Idea', function() {
        beforeEach(function(done) {
            user = new User({
                name: 'Full Name',
                email: 'test@email.com',
                username: 'user',
                password: 'password'
            });

            user.save(function() {
                idea = new Idea({
                    name: 'Idea Name',
                    summary: 'Idea Summary',
                    detail: 'Idea Description',
                    createdBy: user
                });

                done();
            });
        });

        describe('Method Save', function() {
            it('should save without problems', function(done) {
                return idea.save(function(err) {
                    should.not.exist(err);
                    done();
                });
            });

            it('should save with budget', function(done) {
                budget = new Budget({
                    start: 3000,
                    end: 10000
                });
                budget.save(function(err) {
                    should.not.exist(err);
                    idea.budget = budget;
                    idea.save(function(err) {
                        should.not.exist(err);
                        done();
                    });
                });
            });

            it('should save with offerred brands', function(done) {
                var br1 = new Brand({ name: 'Brand 1' });
                br1.save();
                
                var br2 = new Brand({ name: 'Brand 2' });
                br2.save();

                idea.offerredBrands = [br1, br2];
                idea.save(function(err) {
                    should.not.exist(err);
                    idea.offerredBrands.length.should.be.equal(2);

                    br1.remove();
                    br2.remove();
                    done();
                });
            });

            it('should save with categories', function(done) {
                var c1 = new Category({ name: 'Category 1' });
                c1.save();
                
                var c2 = new Category({ name: 'Category 2' });
                c2.save();

                idea.categories = [c1, c2];
                idea.save(function(err) {
                    should.not.exist(err);
                    idea.categories.length.should.be.equal(2);

                    c1.remove();
                    c2.remove();
                    done();
                });
            });

        });

        afterEach(function(done) {
            if(user) user.remove();
            if(brand) brand.remove();
            if(idea) idea.remove();
            if(budget) budget.remove();
            done();
        });

    });
});
