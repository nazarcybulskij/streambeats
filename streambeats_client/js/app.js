define([
    'jquery',
    'underscore',
    'backbone',
    'core/router'
], function($, _, Backbone, Router) {
    var initialize = function() {
        Router.initialize();
    };

    return {
        initialize: initialize
    }
});
