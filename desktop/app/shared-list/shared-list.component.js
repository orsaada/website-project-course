angular.
module('sharedList').
component('sharedList', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/shared-list/shared-list.template.html',
  controller: function ExampleListController($http) {
            var self = this;
            $http.get('/data?_collection=emojies').then(function(response) {
                self.list = response.data;
            });
        }
});