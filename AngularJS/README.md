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
  