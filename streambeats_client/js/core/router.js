define([
    'jquery',
    'underscore',
    'backbone'
], function ($, _, Backbone) {
   var AppRouter = Backbone.Router.extend({
        
        initialize: function () {
            console.log('router initialize...');
        },
        
        routes: {
            '': 'index',
            'tracks/:id': 'tracks'
        },

        index: function (){
            $('.content').html("index");
        }
   });

   var initialize = function (){
        var router = new AppRouter;

        router.on('route:tracks', function(id) {
            $('.content').html("track id: " + id); 
        });

        Backbone.history.start();
   };

   return {
    initialize: initialize
   }
});
