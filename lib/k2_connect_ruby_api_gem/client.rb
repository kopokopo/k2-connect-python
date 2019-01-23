module K2ConnectRubyApiGem
  class Client
    @secret_key
    def initialize(secret_key)
      @secret_key = secret_key
    end

    # Method for comparing the HMAC and with HTTP_X_KOPOKOPO_SIGNATURE
    def authorize_it(message_body, comparison_signature)
      digest = OpenSSL::Digest.new('sha256')
      hmac = OpenSSL::HMAC.hexdigest(digest, @secret_key, message_body)
      puts("\n\nMessage Body: #{message_body}\n\nX-K2-Signature: #{JSON.parse(comparison_signature).join(', ')}\n\n The HMAC hash: #{hmac}")
      puts(hmac.to_s.eql?(JSON.parse(comparison_signature).join(', ')))
    end

    def parse_it_whole(the_res)
      # The Response Body
      hash_body = Yajl::Parser.parse(the_res.request.body.string.to_json)
      # The Response Header
      hash_header = Yajl::Parser.parse(the_res.request.headers.env.select{|k, _| k =~ /^HTTP_/}.to_json)
      # The Response Method
      hash_method = Yajl::Parser.parse(the_res.request.method.to_json)
      hash_header.extend Hashie::Extensions::DeepFind
      # puts ("\n\n The Response Method: #{hash_method}")
      if hash_method.eql?("POST")
        authorize_it(hash_body.to_s, hash_header.deep_select("HTTP_X_KOPOKOPO_SIGNATURE").to_s)
      end
    end
  end
end