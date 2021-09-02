Ok great. It is going to be a fairly simple script.

The framework that we will use is Typer: https://typer.tiangolo.com/

I want to create a JSON:
```
[
	[
		{"id": 1,"full_name":"Firstname Lastname"},
		{"id": 2,"full_name":"Firstname Lastname"},
		{"id": 3,"full_name":"Firstname Lastname"},
		{"id": 4,"full_name":"Firstname Lastname"},
		{"id": 5,"full_name":"Firstname Lastname"},
		{"id": 6,"full_name":"Firstname Lastname"},
		{"id": 7,"full_name":"Firstname Lastname"},
		{"id": 8,"full_name":"Firstname Lastname"},
	],
	[
		{"id": 9,"full_name":"Firstname Lastname"},
		{"id": 10,"full_name":"Firstname Lastname"},
		{"id": 11,"full_name":"Firstname Lastname"},
		{"id": 12,"full_name":"Firstname Lastname"},
		{"id": 13,"full_name":"Firstname Lastname"},
		{"id": 14,"full_name":"Firstname Lastname"},
		{"id": 15,"full_name":"Firstname Lastname"},
		{"id": 16,"full_name":"Firstname Lastname"},
	],
]
```

The ID's will not be sequential, but the. PLD groups will be created like this:

In the CLI command I can supply the projectId and the cohort id.

I will call the intranet API to get the student projects: I will need the project with the id given in the CLI
```
{
  "items": [
    {
      "id": 0,
      "name": "string",
      "completion": 0,
      "score": 0,
      "started_at": "2021-09-02",
      "ended_at": "2021-09-02"
    }
  ],
  "count": 0,
  "next": "string",
  "prev": "string"
}
```
I've already created a script that does the calling. We can reuse that - the output for function will be:
```
[
      {
      "id": 0,
      "name": "string",
      "completion": 0,
      "score": 0,
      "started_at": "2021-09-02",
      "ended_at": "2021-09-02"
      }
]
```
I will create PLD groups based on, 1. their squad and 2. the score after the first deadline for that project.

I have an input CSV - that has all YL's with their squads and cohorts and HolbertonID

I want 7 or 8 YL's in one group - using the scores, matching lower scores and higher scores in the same group.

This will be output as cohort-<id>-project-<id>.json which i can then use to paste in a field for that PLD (edited) 
