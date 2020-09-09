angular.
module('imageList').
component('imageList', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/image-list/image-list.template.html',
  controller: function ImageListController($http) {
            var self = this;
            $http.get('/data?_collection=images&_index=3&_length=4').then(function(response) {
                self.list = response.data;
            });
        }
});