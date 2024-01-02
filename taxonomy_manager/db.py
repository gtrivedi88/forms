apiVersion: tekton.dev/v1
kind: Task
metadata:
  name: vulnerability-scan <.>
  annotations:
	task.output.location: results <.>
	task.results.format: application/json
	task.results.key: SCAN_OUTPUT
spec:
  results:
	- description: CVE result format <.>
  	  name: SCAN_OUTPUT
  	  type: string
  steps:
	- name: scan <.>
  	  image: quay.io/container.image <.> 
  	  env:
    	     - name: TOOL_ENV_VAR1  <.>
      	       valueFrom:
        	           secretKeyRef:
          	               key: tool_var1
          	               name: tool-secrets 
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

<.>  The name of your task.
<.>  The location for storing the task outputs
<.>  The description of the result.
<.> The name of the vulnerability scanning tool that you have used. For example, you can use Roxctl. 
<.> The location of the actual image containing the scan tool.
<.> The tool-specific environment variables
<.>     Set up the shell script to be executed. You must ensure that the scan results are outputted in the json format. For example, scan_output.json.
<.>  Extract vulnerability summary (adjust jq command for different JSON structures).
