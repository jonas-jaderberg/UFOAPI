/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
    /// <summary>
    /// 
    /// </summary>
    [DataContract]
    public partial class AlertCLinearByCode : IEquatable<AlertCLinearByCode>
    {
        /// <summary>
        /// Gets or Sets AlertCLocationCountryCode
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="alertCLocationCountryCode", EmitDefaultValue=false)]
        public string AlertCLocationCountryCode { get; set; }

        /// <summary>
        /// Gets or Sets AlertCLocationTableNumber
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="alertCLocationTableNumber", EmitDefaultValue=false)]
        public string AlertCLocationTableNumber { get; set; }

        /// <summary>
        /// Gets or Sets AlertCLocationTableVersion
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="alertCLocationTableVersion", EmitDefaultValue=false)]
        public string AlertCLocationTableVersion { get; set; }

        /// <summary>
        /// Gets or Sets AlertCDirection
        /// </summary>
        [Required]
        [DataMember(Name="alertCDirection", EmitDefaultValue=false)]
        public AlertCDirection AlertCDirection { get; set; }

        /// <summary>
        /// Gets or Sets LocationCodeForLinearLocation
        /// </summary>
        [Required]
        [DataMember(Name="locationCodeForLinearLocation", EmitDefaultValue=false)]
        public AlertCLocation LocationCodeForLinearLocation { get; set; }

        /// <summary>
        /// Gets or Sets AlertCLinearExtensionG
        /// </summary>
        [DataMember(Name="alertCLinearExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> AlertCLinearExtensionG { get; set; }

        /// <summary>
        /// Gets or Sets AlertCLinearByCodeExtensionG
        /// </summary>
        [DataMember(Name="alertCLinearByCodeExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> AlertCLinearByCodeExtensionG { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AlertCLinearByCode {\n");
            sb.Append("  AlertCLocationCountryCode: ").Append(AlertCLocationCountryCode).Append("\n");
            sb.Append("  AlertCLocationTableNumber: ").Append(AlertCLocationTableNumber).Append("\n");
            sb.Append("  AlertCLocationTableVersion: ").Append(AlertCLocationTableVersion).Append("\n");
            sb.Append("  AlertCDirection: ").Append(AlertCDirection).Append("\n");
            sb.Append("  LocationCodeForLinearLocation: ").Append(LocationCodeForLinearLocation).Append("\n");
            sb.Append("  AlertCLinearExtensionG: ").Append(AlertCLinearExtensionG).Append("\n");
            sb.Append("  AlertCLinearByCodeExtensionG: ").Append(AlertCLinearByCodeExtensionG).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            if (obj is null) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((AlertCLinearByCode)obj);
        }

        /// <summary>
        /// Returns true if AlertCLinearByCode instances are equal
        /// </summary>
        /// <param name="other">Instance of AlertCLinearByCode to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AlertCLinearByCode other)
        {
            if (other is null) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    AlertCLocationCountryCode == other.AlertCLocationCountryCode ||
                    AlertCLocationCountryCode != null &&
                    AlertCLocationCountryCode.Equals(other.AlertCLocationCountryCode)
                ) && 
                (
                    AlertCLocationTableNumber == other.AlertCLocationTableNumber ||
                    AlertCLocationTableNumber != null &&
                    AlertCLocationTableNumber.Equals(other.AlertCLocationTableNumber)
                ) && 
                (
                    AlertCLocationTableVersion == other.AlertCLocationTableVersion ||
                    AlertCLocationTableVersion != null &&
                    AlertCLocationTableVersion.Equals(other.AlertCLocationTableVersion)
                ) && 
                (
                    AlertCDirection == other.AlertCDirection ||
                    AlertCDirection != null &&
                    AlertCDirection.Equals(other.AlertCDirection)
                ) && 
                (
                    LocationCodeForLinearLocation == other.LocationCodeForLinearLocation ||
                    LocationCodeForLinearLocation != null &&
                    LocationCodeForLinearLocation.Equals(other.LocationCodeForLinearLocation)
                ) && 
                (
                    AlertCLinearExtensionG == other.AlertCLinearExtensionG ||
                    AlertCLinearExtensionG != null &&
                    other.AlertCLinearExtensionG != null &&
                    AlertCLinearExtensionG.SequenceEqual(other.AlertCLinearExtensionG)
                ) && 
                (
                    AlertCLinearByCodeExtensionG == other.AlertCLinearByCodeExtensionG ||
                    AlertCLinearByCodeExtensionG != null &&
                    other.AlertCLinearByCodeExtensionG != null &&
                    AlertCLinearByCodeExtensionG.SequenceEqual(other.AlertCLinearByCodeExtensionG)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                var hashCode = 41;
                // Suitable nullity checks etc, of course :)
                    if (AlertCLocationCountryCode != null)
                    hashCode = hashCode * 59 + AlertCLocationCountryCode.GetHashCode();
                    if (AlertCLocationTableNumber != null)
                    hashCode = hashCode * 59 + AlertCLocationTableNumber.GetHashCode();
                    if (AlertCLocationTableVersion != null)
                    hashCode = hashCode * 59 + AlertCLocationTableVersion.GetHashCode();
                    if (AlertCDirection != null)
                    hashCode = hashCode * 59 + AlertCDirection.GetHashCode();
                    if (LocationCodeForLinearLocation != null)
                    hashCode = hashCode * 59 + LocationCodeForLinearLocation.GetHashCode();
                    if (AlertCLinearExtensionG != null)
                    hashCode = hashCode * 59 + AlertCLinearExtensionG.GetHashCode();
                    if (AlertCLinearByCodeExtensionG != null)
                    hashCode = hashCode * 59 + AlertCLinearByCodeExtensionG.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(AlertCLinearByCode left, AlertCLinearByCode right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(AlertCLinearByCode left, AlertCLinearByCode right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}
