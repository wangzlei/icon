region=${AWS_REGION-$(aws configure get region)}
cat release-note.md | grep $region | sed "s/[ ]//g;s/\|//g" | sed "s/^$region//"