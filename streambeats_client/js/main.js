require.config({
    paths: {
        'jquery': '../bower_components/jquery/dist/jquery',
        'underscore': '../bower_components/underscore/underscore',
        'backbone': '../bower_components/backbone/backbone'
    },

    shine: {
        'jquery': {
            'deps': [],
            'exports': '$'
        },
        'underscore': {
            'deps': [],
            'exports': '_'
        },
        'backbone': {
            'deps': ['jquery', 'underscore'],
            'exports': 'Backbone'
        }
    }
});

require([
    'app'
], function(App) {
    App.initialize();
});
