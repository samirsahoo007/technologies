var app = angular.module('app', ['app.model', 'app.controller'])
        .run(function ( $rootScope, $log, Model ) {

            $log.log('App started.');
            // Model.setVariable('Variable updated.');

            $rootScope.version = Model.getVersion();
            $rootScope.setUp = function () {
                Model.setVariable( Model.getVariable() + 1 );
            };

            document.getElementById('loading').innerHTML = Model.getMyData();
            document.getElementById('headline').innerHTML = Model.getVariable() + ' ' + Model.getConstant();
        })
    ;