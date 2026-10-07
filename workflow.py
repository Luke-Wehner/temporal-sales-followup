from datetime import timedelta

from temporalio import workflow


@workflow.defn
class SalesFollowUpWorkflow:
    @workflow.run
    async def run(self, prospect_name: str) -> str:
        # Step 1: A prospect enters the sales follow-up process.
        workflow.logger.info(
            f"Starting follow-up workflow for {prospect_name}"
        )

        # Step 2: Temporal durably waits before the next follow-up.
        # For this demo we use 10 seconds instead of several days.
        await workflow.sleep(timedelta(seconds=10))

        # Step 3: The workflow resumes automatically after the wait.
        message = (
            f"Follow up with {prospect_name}: "
            "send the next personalized sales touchpoint."
        )

        workflow.logger.info(message)

        return message
