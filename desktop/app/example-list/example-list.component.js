angular.
module('exampleList').
component('exampleList', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/example-list/example-list.template.html',
  controller: function ExampleListController($http) {
            var self = this;
             $http.get('/data?_collection=images&_index=3&_length=4').then($http.get('/data?_collection=dogs').then(function(response) {
                self.list = response.data;
            }));
        }
});