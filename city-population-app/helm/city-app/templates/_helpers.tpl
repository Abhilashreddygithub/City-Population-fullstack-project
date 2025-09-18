{{/*
Common chart helper templates
*/}}
{{- define "city-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "city-app.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name (include "city-app.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
