# Common Class Behaviours for stk, pay and transfers
class K2Entity
  attr_accessor :access_token, :the_array
  attr_reader :k2_response_body, :query_hash, :location_url
  include K2Validation, K2Utilities

  # Initialize with access token from Subscriber Class
  def initialize(access_token)
    @access_token = access_token
    @threads = []
    @exception_array = %w[authenticity_token]
  end

  # Query/Check the status of a previously initiated request
  def query_status(class_type, path_url)
    query(class_type, path_url)
  end

  # Query Location URL
  def query_resource(class_type, url)
    query(class_type, url)
  end

  def query(class_type, path_url)
    # TODO: Add back the validation to ensure only https location urls are returned
    # path_url = validate_url(@location_url)
    query_hash = make_hash(path_url, 'get', @access_token, class_type, nil)
    @threads << Thread.new do
      sleep 0.25
      @k2_response_body = K2Connect.make_request(query_hash)
    end
    @threads.each(&:join)
  end
end
