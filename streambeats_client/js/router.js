define([
    'jquery',
    'underscore',
    'backbone'
], function ($, _, Backbone) {
   var AppRouter = Backbone.Router.extend({
        routes: {
            '': 'index',
            'tracks': 'tracks'
        },

        index: function (){
            console.log('index');
        }
   });

   var initialize = function (){
        var router = new AppRouter;

        router.on('route:tracks', function () {
            console.log('tracks'); 
        });

        Backbone.history.start();
   };

   return {
    initialize: initialize
   }
});
