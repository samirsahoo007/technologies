Where I've used:
----------------
Login Application
Upload File
Nav Menu
Switch Menu
Search Tab
Drag Application
Timer Application

Other applications:
        Order Form
        Cart Application
        Bootstrap Application
        Translate Application
        Chart Application
        Maps Application
        Share Application
        Weather Application
        Leaflet Application
        Lastfm Application
        ToDo Application
        Notepad Application

Using AngularJS
===============

Website: [https://angularjs.org/](https://angularjs.org/)

Docs: [https://docs.angularjs.org/guide](https://docs.angularjs.org/guide)


Init with Module
-----------
See [`main-module.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-main-module-js)
  ```html
  <html ng-app="app">
  ```
  
Manual bootstrap with Module
-----------
See [`bootstrap.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-bootstrap-js) and [`main-module.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-main-module-js)
  ```html
  <div id="loading">Loading...</div>
  ```

Controller
-----------
See [`controller.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-js) and after that [`controller-module.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-module-js)
  ```html
  <div ng-controller="ctrl">
    <h1>{{ headline }}</h1>
  </div>
  ```
  
Controller with Scope
-----------
See [`controller-module.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-module-js)
  ```html
  <div ng-controller="Controller">
    <p ng-bind="sayHello"></p>
  </div>
  ```
  
Controller with Scope and method binding
-----------
See [`controller-module.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-module-js)
  ```html
  <div ng-controller="Controller">
    <p ng-bind="getHelloExpression()"></p>
    <button ng-click="click()">Make Click</button>
  </div>
  ```  

Root Scope  
-----------
See [`main-module.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-main-module-js)
  ```html
    <p>{{ version }}</p>
  ```
  
Filter 
-----------  
See [default filters](https://docs.angularjs.org/api/ng/filter)
  ```html
    <p>{{ prodct.price | currency }}</p>
    <p>{{ prodct.pubdate | date }}</p>
  ```
  
Controller Hierarchy  
-----------
See [`controller-module.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-module-js)
  ```html
  <div ng-controller="Controller">
    <p ng-bind="getHelloExpression()"></p>
    <button ng-click="click()" ng-controller="ButtonController">{{ label }}</button>
  </div>
  ``` 

List / Repeat
-----------
See [`controller.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-js)
  ```html
  <ul class="unstyled">
    <li ng-repeat="item in items">{{ item.name }}</li>
  </ul>
  ```

Inline styles
-----------
See [`controller.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-js)

Using `style="font-size:{{ item.val }}px"` will only work for IE <= 11; `ng-style` is supported down to IE8.
   ```html
  <ul class="unstyled">
    <li ng-repeat="item in items" ng-style="{'fontSize':(item.val+'px')}">{{ item.name }}</li>
  </ul>
  ``` 
  
Bidirectional binding
-----------
See [`controller.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-js)
  ```html
  <form class="form-horizontal">
    <input type="text" ng-model="input"/>
  </form>
  <p>Your input: {{ input }}</p>
  ```
  
Click event
-----------
See [`controller.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-js)
  ```html
  <button class="btn" ng-click="add()">Add</button>
  ```
  
Method binding
-----------
See [`controller.js`](https://gist.github.com/hofmannsven/d67f0cb2f67911a438ed#file-controller-js)
  ```html
  <p>Available items: {{ getItemsLenght() }}</p>
  ```
  
Example
-------

ng-app Sets the AngularJS section.
ng-controller Attaches a controller class to the view.
ng-init Sets a default variable value.
ng-bind Alternative to {{ }} template.
ng-bind-template Binds multiple expressions to the view.
ng-click Executes a method or expression when element is clicked.
ng-repeat Used to loop through each item in a collection to create a new template.
ng-model Binds an input,select, textarea etc elements with model property.
ng-selected Used to set selected option in element.
ng-checked Sets the checkbox.
ng-href Dynamically bind AngularJS variables to the href attribute.
ng-form Sets a form
ng-disabled Controls the form element's disabled property
ng-show/ng-hide Show/Hide elements based on an expression.
ng-switch Conditionally switch control based on matching expression.
ng-readonly Used to set readonly attribute to an element.
ng-cut Used to specify custom behavior on cut event.
ng-copy Used to specify custom behavior on copy event.
ng-paste Used to specify custom behavior on paste event.
ng-if Remove or recreates an element in the DOM depending on an expression
ng-value Bind angular expressions to the value of .
ng-required Bind angular expressions to onsubmit events.
ng-submit Bind angular expressions to onsubmit events.
ng-change Evaluates specified expression when the user changes the input.
ng-list Used to convert string into list based on specified delimiter.

ng-non-bindable States that the data isn't bindable.
ng-bind-html Binds inner HTML property of an HTML element.
ng-class Sets the css class dynamically.
ng-cloak Prevents displaying the content until AngularJS has taken control.
ng-include Used to fetch, compile and include an external HTML fragment to your page.
ng-src Dynamically bind AngularJS variables to the src attribute.
ng-style Sets CSS style on an HTML element.
ng-pattern Adds the pattern validator to ngModel.
ng-maxlength Adds the maxlength validator to ngModel.
ng-minlength Adds the minlength validator to ngModel.
ng-classeven Works in conjunction with ngRepeat and take effect only on odd (even) rows.
ng-classodd Works in conjunction with ngRepeat and take effect only on odd (even) rows.
ng-options Used to dynamically generate a list of elements for the element.
ng-open Used to set the open attribute on the element, if the expression inside ngOpen is truthy.
