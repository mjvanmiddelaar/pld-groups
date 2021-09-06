## Create PLD groups

Add cohort.csv in your local env.

Run

```shell
./create-pld-group <project_id> <cohort> <mock>>
```

To test, add sample yls to sample.csv and run:

```shell
./create-pld-group 19 sample true
```

The result output is in cohort-sample-project-19.json. 

In the test run, the scores are added to the endresult json **cohort-sample-project-19.json** to
verify that the script works