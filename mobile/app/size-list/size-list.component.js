angular.
module('sizeList').
component('sizeList', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/size-list/size-list.template.html',
  controller: function SizeListController($http) {
            var self = this;
            this.size = "big";
            $http.get('/data?_collection=sizes').then(function(response) {
                self.list = response.data;
            });
        }
});