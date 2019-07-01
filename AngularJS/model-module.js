var Model = function( $log, myVariable, myConstant, version ) {
    $log.log('New singleton instance of model.');
    return {
        getMyData : function() {
            return 'Ready.';
        },
        getVariable : function() {
            return myVariable;
        },
        setVariable : function( val ) {
            myVariable = val;
        },
        getConstant : function() {
            return myConstant;
        },
        getVersion : function() {
            return version;
        }
    }
};

var model = angular.module('app.model', [])
        .value('myVariable', 1)
        .constant('myConstant', 'My constant.')
        .constant('version', '1.0.0')

        .factory('Model', Model) // also via .service()
    ;