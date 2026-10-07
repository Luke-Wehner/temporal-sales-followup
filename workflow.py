from datetime import timedelta
from temporalio import workflow

@workflow.defn
class SalesFollowUpWorkflow:
    @workflow.run
    async def run(self, prospect_name: str) -> str:
        workflow.logger.info(f"Starting follow-up for {prospect_name}")

        await workflow.sleep(timedelta(seconds=10))

        message = f"Follow up with {prospect_name}: send the next personalized sales touchpoint."
        workflow.logger.info(message)

        return message
