Enhancing OpenShift Pipelines with Software Supply Chain Security Use Cases

The PipelineRun Details view in the Developer or Administrator perspective of the web console provides an enhanced visual representation of PipelinesRuns within a project. 

For a PipelineRun Details, you can now view:

Vulnerabilities Link to SBOM for PipelineRuns
Add a badge/icon for chains.tekton.dev/signed=true for PipelineRuns
Move pipelinerun results section to output tab using static tab extension point.


Viewing Vulnerabilities
The Vulnerabilities row in the PipelineRun details view of the web console provides a visual representation of all the vulnerabilities within a project, for example, critical, high, medium low.

Additionally you can review the Vulnerabilities column in the PipelineRuns view as well.

To view the Vulnerabilities in your project complete the following steps.

Prerequisites
You have logged in to the web console.


You have the appropriate roles and permissions in a project to create applications and other workloads in OpenShift Container Platform.


You have created and deployed an application on OpenShift Container Platform using the Administrator or Developer perspective.


You are in the Administrator or Developer perspective.
You have a vulnerability scan task and the results are stored in the JSON file. You have to update your vulnerability scan task in the following format:



Procedure
Update the vulnerability scan task yaml file to ensure it stores the output in the json file and extracts in the following format:
Example vulnerability scan task

		apiVersion: tekton.dev/v1
kind: Task
metadata:
  name: vulnerability-scan
  annotations:
	task.output.location: results
	task.results.format: application/json
	task.results.key: SCAN_OUTPUT
spec:
  results:
	- description: The Common Vulnerabilities and Exposures (CVE) result format
  	  name: SCAN_OUTPUT
  	  type: string
  steps:
	- name: scan
  	  mage: IMAGE_PLACEHOLDER  # Replace with the actual image containing the scan tool
  	  env:
    	     - name: TOOL_ENV_VAR1  # Replace with tool-specific environment variables
      	       valueFrom:
        	           secretKeyRef:
          	               key: tool_var1
          	               name: tool-secrets  # Replace with the actual secret name
  	script: | <.>
    	
#!/bin/sh
    	# Tool-specific setup 
    	
jq -rce \ <.>
    	"{vulnerabilities:{
    	critical: (.result.summary.CRITICAL),
    	high: (.result.summary.IMPORTANT),
    	medium: (.result.summary.MODERATE),
    	low: (.result.summary.LOW)
    	}}" scan_output.json | tee $(results.SCAN_OUTPUT.path)
<.>     Set up the shell script to be executed. For example, you use Roxctl as your vulnerability scanning tool. You must ensure that the scan results are outputted in the json format. For example, scan_output.json.
<.>  Extract vulnerability summary (adjust jq command for different JSON structures).

Update your piplelinerun to add vulnerabilities specifications:
	…
spec:
  results:
	- description: The common vulnerabilities and exposures (CVE) result
  	name: SCAN_OUTPUT
  	value: $(tasks.vulnerability-scan.results.SCAN_OUTPUT)
