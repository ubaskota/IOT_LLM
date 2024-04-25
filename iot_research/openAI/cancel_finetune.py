import openai

api_key = "sk-WugXI9hNrh2SBFeWyx" 
fine_tune_id = "ftjob-l85LioJG"

if __name__ == "__main__":
  cancel_tune = cancel_fine_tune(
    fine_tune_id,
    openai_api_key = Sys.getenv(api_key),
    openai_organization = NULL
  )

  print(cancel_tune)




  # curl -X POST https://api.openai.com/v1/fine-tunes/file-Ws3lEBf82IX7YXoGob13pR0k/cancel \
  # -H "Authorization: Bearer sk-WugXI9hrCLOZfSqmuUvwE"
