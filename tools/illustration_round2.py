"""Round 2 configuration for the verified local image-ingestion pipeline."""
import illustration_batch as pipeline
import sys
pipeline.IDS=['B012','B015','B023','B025','B029','B033','B054','B070','B078','B104','B116','B120']
pipeline.BATCH='round2-dpl-ill-1.2-v01'
pipeline.VERSION='v01'
pipeline.STYLE='DPL-ILL-1.2'
if __name__=='__main__':
 assert sys.argv[1]=='ingest'
 pipeline.ingest(sys.argv[2],sys.argv[3])
