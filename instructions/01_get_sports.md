# get_sports Function Documentation

## Overview
The `get_sports` function retrieves a list of in-season sport objects from the Odds API. This function does not count against your usage quota.

## API Endpoint
```
GET /v4/sports/?apiKey={apiKey}
```

## Parameters
- `api_key` (string, required): Your API key, emailed when you sign up for a plan
- `all` (boolean, optional): If set to true (`all=true`), returns a list of all sports including in-season and out-of-season sports. Defaults to `false`

## Example Request
```
GET https://api.the-odds-api.com/v4/sports/?apiKey=YOUR_API_KEY
```

## Response
The response will be a list of sport dictionaries. Each dictionary contains:

| Field | Type | Description |
|-------|------|-------------|
| `key` | string | Unique sport identifier (e.g., 'americanfootball_nfl') |
| `group` | string | Sport category (e.g., 'American Football') |
| `title` | string | Sport name (e.g., 'NFL') |
| `active` | boolean | Indicates if sport is currently in season |
| `has_outrights` | boolean | Indicates if sport has outright (futures) markets |

## Response Headers
| Header | Description |
|--------|-------------|
| `x-requests-remaining` | Number of requests remaining before quota reset |
| `x-requests-used` | Number of requests used since last quota reset |
| `x-requests-last` | Usage cost of the last API call |

## Usage Notes
- Use this function as a first step to understand available sports
- The sport key from the response can be used for subsequent odds data requests using the `/odds` endpoint
- Setting `all=false` (default) returns only in-season sports