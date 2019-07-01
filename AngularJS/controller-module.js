function Controller( $scope, $log, Model ) {
    $log.log( 'Controller instance for view.' );
    $scope.sayHello = 'Hello world!';
    $scope.label = 'Default label';

    /*
    // Default within $scope
    $scope.click = function () {
        Model.setVariable( Model.getVariable() + 1 );
    };
    */

    // Prepare to leave $scope
    this.model = Model;
    var that = this;
    $scope.click = function () {
        that.onClick();
    };

    $scope.getHelloExpression = function () {
      return $scope.sayHello + ' #' + Model.getVariable();
    };

    this.scope = $scope;

}

var ctrl = Controller.prototype;

ctrl.onClick = function () {
    // Call setUp() from root scope
    this.scope.$root.setUp();
};

function ButtonController( $scope, $log, Model ) {
    // Overwrite parent label
    $scope.label = 'Custom label';

    // Overwrite parent click()
    this.scope = $scope;
    var that = this;
    $scope.click = function() {
        that.onClick();
    }

}

var btnctrl = ButtonController.prototype;

btnctrl.onClick = function () {
    console.log('Clicked.');
    // Call parent click()
    this.scope.$parent.click();
};

var controller = angular.module('app.controller', ['app.model'])
    .controller( 'Controller', Controller )
    .controller( 'ButtonController', ButtonController )
    ;