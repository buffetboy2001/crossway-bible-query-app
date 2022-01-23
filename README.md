# bible-api-query

A personal project to use python code to pull passages from online.

## Secrets

The crossway api requires an API Token to work. Get your own at: https://api.esv.org/docs/.

This code assumes that the API Token is stored in a JSON file. (The token should _not be stored in a public repo_.) The secrets file should be provided to the application as a command line argument.
## Example

You can run `python/example_script.py` from the command line. It will generate a query for a random chapter/verse from the book of Proverbs. 

```bash
python/example_script.py ./secrets.json
```

A successful query will return something like this:
```bash
By me kings reign, and rulers decree what is just; – Proverbs 8:15
```