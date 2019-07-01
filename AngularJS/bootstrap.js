var intID;
intID = setInterval( function() {
    if ( /loaded|complete/i.test(document.readyState) ) {
        angular.bootstrap( document, ['app'] );
        clearInterval( intID );
    }
}, 10 );