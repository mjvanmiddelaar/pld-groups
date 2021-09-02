""" create automaticaly pld-groups """
import typer


App = typer.Typer()

@App.command()
def basecommand(project_id: int, cohort_id: int):
    """  
    Get the project id and the cohort id 
    to collect data and to create pld-groups 
    """
    print(f'chohort Id: {cohort_id}, projectId: {project_id}')

if __name__ == "__main__":
    App()
