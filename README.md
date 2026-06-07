# crossway bible api queries

A personal project to use python code to pull passages from online.

## Secrets

The crossway api requires an API Token to work. Get your own at: https://api.esv.org/docs/.

This code assumes that the API Token is stored in a JSON file. (The token should _not be stored in a public repo_.) The secrets file should be provided to the application as a command line argument.

```json
{ "token" : "my-api-key" }
```

## Example

You can run [src/example_script.py](./src/example_script.py) from the command line. It will generate a query for a random chapter/verse from the book of Proverbs. 

```bash
uv run src/example_script.py ./secrets.json
```

A successful query will return something like this:
```bash
He will not always chide, nor will he keep his anger forever. He does not deal with us according to our sins, nor repay us according to our iniquities. For as high as the heavens are above the earth, so great is his steadfast love toward those who fear him; as far as the east is from the west, so far does he remove our transgressions from us. - Psalm 103:9–12
```

~ Enjoy ~