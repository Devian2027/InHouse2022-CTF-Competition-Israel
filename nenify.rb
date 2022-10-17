post '/' do
  if params[:neon] =~ /^[0-9a-z ]+$/i
    @neon = ERB.new(params[:neon]).result(binding)
  else
    @neon = "Malicious Input Detected"
  end
  erb :'index'
end