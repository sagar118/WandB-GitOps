import wandb, os
import wandb.apis.reports as wr

assert os.getenv('WANDB_API_KEY'), "WANDB_API_KEY must be set in environment variable"

def get_baseline_scores(entity='sagar118',
                        project='cicd-quickstart',
                        tag='baseline'):
    "Get the baseline run from the project using tags"

    api = wandb.Api()
    run = api.runs(f'{entity}/{project}', {'tags': {'$in': [tag]}})
    assert len(run) == 1
    return run[0]

def comapre_runs(entity='sagar118',
                project='cicd-quickstart',
                tag='baseline',
                run_id=None):
    "Compare the current run with the baseline run"

    entity = os.getenv('WANDB_ENTITY', entity)
    project = os.getenv('WANDB_PROJECT', project)
    tag = os.getenv('BASELINE_TAG', tag)
    run_id = os.getenv('RUN_ID', run_id)

    print(run_id)
    assert run_id, 'Run id must be present in the enironment variable or passed as an arguement'
    
    return ""

#     baseline = get_baseline_scores(entity, project, tag)
#     report = wr.Report(project=project, title="Compare Baseline vs Latest Run")
    
#     panel_grids = wr.PanelGrid(
#         runsets=[
#             wr.Runset(entity, project, "Run Comparison").set_filters_with_python_expr(f"ID in ['{run_id}', '{baseline.id}']")
#         ],
#         panels = [
#             wr.RunComparer(diff_only='split', layout={'w': 24, 'h': 15})
#         ]
#     )

#     plots = wr.PanelGrid(
#         panels=[
#             wr.LinePlot(x='Step', y=['acc'], smoothing_factor=0.8),
#             wr.LinePlot(x='Step', y=['loss'], smoothing_factor=0.8),
#             wr.LinePlot(x='Step', y=['val_acc'], smoothing_factor=0.8),
#             wr.LinePlot(x='Step', y=['val_loss'], smoothing_factor=0.8),
#         ]
#     )
#     report.blocks = report.blocks[:1] + [panel_grids] + [plots] + report.blocks[1:]
#     report.save()

#     if os.getenv("CI"):
#         with open(os.environ['GITHUB_OUTPUT'], 'a') as handle:
#             print(f"REPORT_URL={report.url}", file=handle)
#     return report.url
    
if __name__ == '__main__':
    print(f"The comparison report can be found at: {comapre_runs()}")
