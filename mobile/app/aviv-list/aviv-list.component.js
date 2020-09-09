angular.
module('avivList').
component('danielList', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'app/aviv-list/aviv-list.template.html',
  controller: function AvivListController($http) {
            var self = this;
            $http.get('/data?_collection=cities').then(function(response) {
                self.list = response.data;
            });
        }
});