function ctrl( $scope ) {

    $scope.headline = 'Headline';

    $scope.items = [
        { name: 'Item 1', val: 10 },
        { name: 'Item 2', val: 12 },
        { name: 'Item 3', val: 14 },
        { name: 'Item 4', val: 16 }
    ];
    
    $scope.product = {
  	    price: 19,
        pubdate: new Date('2015', '08', '01')
    }

    $scope.getItemsLenght = function () {
        return $scope.items.length;
    };

    $scope.input = 'Username';

    $scope.add = function () {
        $scope.items.push( { name:$scope.input, val:10 } );
    };

}